""" Sonos Player Modes """
import logging
from homeassistant.components import sonos

_LOGGER = logging.getLogger(__name__)

DOMAIN = "sonos_crossfade"

DEPENDENCIES = ["sonos"]


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    sonos_crossfade = SonosPlayerData(hass)
    hass.services.register(DOMAIN, "update", sonos_crossfade.update)

    _LOGGER.debug("Started Sonos Crossfade")

    return True


class SonosPlayerData(object):
    """Controls Sonos Speakers discovered by the Sonos Integration."""

    def __init__(self, hass):
        """Initialize the data object."""
        self.hass = hass

    def get_soco_from_entity_id(self, entity_id):
        """Returns the SoCo object of the entity that corresponds to the given entity_id"""
        data_sonos = self.hass.data[sonos.media_player.DATA_SONOS]

        for entity in data_sonos.entities:
            if entity.entity_id == entity_id:
                break
        else:
            entity = None

        if entity is None:
            _LOGGER.error("No entity found for entity_id: %s", entity_id)
            return None

        return entity.soco

    def update(self, call):
        """Handle the service call."""
        enabled = call.data.get("enabled", "true")
        entity_id = call.data.get("entity_id", "media_player.bedroom")

        device = self.get_soco_from_entity_id(entity_id)

        if device is not None:
            device.cross_fade = enabled
