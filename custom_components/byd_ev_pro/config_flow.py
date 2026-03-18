"""Config flow and options flow for BYD EV Pro integration."""

from __future__ import annotations

import secrets
from typing import Any

import voluptuous as vol

from homeassistant.components.webhook import async_generate_url
from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
    OptionsFlowWithConfigEntry,
)
from homeassistant.core import callback
from homeassistant.helpers import selector

from .const import DOMAIN


class BydEvProConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for BYD EV Pro."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow:
        """Return the options flow handler."""
        return BydEvProOptionsFlow(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Ask the user for a vehicle name."""
        if user_input is not None:
            vehicle_name = user_input["vehicle_name"]
            webhook_id = f"byd_ev_pro_{secrets.token_hex(16)}"

            self._webhook_id = webhook_id
            self._vehicle_name = vehicle_name

            return self.async_show_form(
                step_id="webhook_info",
                data_schema=vol.Schema({}),
                description_placeholders={
                    "webhook_url": async_generate_url(
                        self.hass, webhook_id
                    ),
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        "vehicle_name", default="Song Plus EV"
                    ): str,
                }
            ),
        )

    async def async_step_webhook_info(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Show webhook URL and finish setup."""
        if user_input is not None:
            return self.async_create_entry(
                title=self._vehicle_name,
                data={"webhook_id": self._webhook_id},
                options={"token": "", "webhook_secret": "", "actions": []},
            )

        return self.async_show_form(
            step_id="webhook_info",
            data_schema=vol.Schema({}),
            description_placeholders={
                "webhook_url": async_generate_url(
                    self.hass, self._webhook_id
                ),
            },
        )


class BydEvProOptionsFlow(OptionsFlowWithConfigEntry):
    """Handle options for BYD EV Pro — token, secret, voice action CRUD."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Show menu: settings, add action, remove action."""
        return self.async_show_menu(
            step_id="init",
            menu_options=["settings", "add_action", "remove_action"],
        )

    async def async_step_settings(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Edit token and webhook secret."""
        if user_input is not None:
            actions = self.options.get("actions", [])
            return self.async_create_entry(
                data={
                    "token": user_input.get("token", ""),
                    "webhook_secret": user_input.get("webhook_secret", ""),
                    "actions": actions,
                }
            )

        token = self.options.get("token", "")
        webhook_secret = self.options.get("webhook_secret", "")
        actions = self.options.get("actions", [])

        # Build action summary for display.
        if actions:
            lines = [
                f"• **{a['voice_phrase_en']}** → `{a['domain']}.{a['service']}` on `{a['entity_id']}`"
                for a in actions
            ]
            action_summary = "\n".join(lines)
        else:
            action_summary = "_No voice actions configured._"

        return self.async_show_form(
            step_id="settings",
            data_schema=vol.Schema(
                {
                    vol.Optional("token", default=token): str,
                    vol.Optional("webhook_secret", default=webhook_secret): str,
                }
            ),
            description_placeholders={
                "action_summary": action_summary,
            },
        )

    async def async_step_add_action(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Add a new voice action — simplified to 1 required + 4 optional fields."""
        if user_input is not None:
            # Script entity_id is "script.gate_open" → domain=script, service=gate_open
            ha_action = user_input["ha_action"]
            _, _, service = ha_action.partition(".")

            actions = list(self.options.get("actions", []))
            actions.append(
                {
                    "id": f"ha_{secrets.token_hex(4)}",
                    "domain": "script",
                    "service": service,
                    "entity_id": "",
                    "service_data": "",
                    "voice_phrase_uk": user_input.get("voice_phrase_uk", ""),
                    "voice_phrase_en": user_input.get("voice_phrase_en", ""),
                    "confirmation_uk": user_input.get("confirmation_uk", ""),
                    "confirmation_en": user_input.get("confirmation_en", ""),
                }
            )
            token = self.options.get("token", "")
            ws = self.options.get("webhook_secret", "")
            return self.async_create_entry(
                data={"token": token, "webhook_secret": ws, "actions": actions}
            )

        # List all script entities as options.
        script_states = self.hass.states.async_all("script")
        script_options = [
            selector.SelectOptionDict(
                value=s.entity_id,
                label=f"{s.attributes.get('friendly_name', s.entity_id)} ({s.entity_id})",
            )
            for s in sorted(script_states, key=lambda s: s.entity_id)
        ]

        return self.async_show_form(
            step_id="add_action",
            data_schema=vol.Schema(
                {
                    vol.Required("ha_action"): selector.SelectSelector(
                        selector.SelectSelectorConfig(
                            options=script_options,
                            mode=selector.SelectSelectorMode.DROPDOWN,
                        )
                    ),
                    vol.Optional("voice_phrase_uk", default=""): selector.TextSelector(),
                    vol.Optional("voice_phrase_en", default=""): selector.TextSelector(),
                    vol.Optional("confirmation_uk", default=""): selector.TextSelector(),
                    vol.Optional("confirmation_en", default=""): selector.TextSelector(),
                }
            ),
        )

    async def async_step_remove_action(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Remove a voice action by selection."""
        actions = list(self.options.get("actions", []))

        if user_input is not None:
            selected = user_input.get("action_index")
            if selected is not None:
                idx = int(selected)
                if 0 <= idx < len(actions):
                    actions.pop(idx)
            token = self.options.get("token", "")
            ws = self.options.get("webhook_secret", "")
            return self.async_create_entry(
                data={"token": token, "webhook_secret": ws, "actions": actions}
            )

        if not actions:
            return self.async_abort(reason="no_actions")

        action_labels = {
            str(i): f"{a['voice_phrase_en']} → {a['domain']}.{a['service']}"
            for i, a in enumerate(actions)
        }

        return self.async_show_form(
            step_id="remove_action",
            data_schema=vol.Schema(
                {
                    vol.Required("action_index"): vol.In(action_labels),
                }
            ),
        )
