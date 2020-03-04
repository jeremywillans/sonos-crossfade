# Sonos Crossfade

## Custom Component For Home Assistant

[![gh_release][gh_release]](../../releases)
[![gh_last_commit][gh_last_commit]](../../commits/master)
[![hacs_custom][hacs_custom]][hacs]

This component creates a service `sonos_crossfade.update` that lets you change the crossfade setting on any one of your Sonos speakers. Requires the `sonos` component to be already setup.

## Install
1. Install with [HACS](https://github.com/custom-components/hacs) or copy the `custom_components` folder in your HA configuration folder.
2. Add
    ```
    event_emitter:
    ```
    to the `configuration.yaml`

## Service Parameters
- `entity_id`: entity id of the speaker  (eg. `media_player.bedroom`)
- `enabled`: crossfade state.

## Support

In case you've found a bug, please [open an issue on GitHub](../../issues).

## My Repos

[ha-rest980-roomba] | 
[roomba-vacuum-card] | 
[hass-addons] | 
[event-emitter] | 
[sonos-crossfade]

[![BMC]](https://www.buymeacoffee.com/jeremywillans)

[gh_release]: https://img.shields.io/github/v/release/jeremywillans/sonos-crossfade.svg?style=for-the-badge
[gh_last_commit]: https://img.shields.io/github/last-commit/jeremywillans/sonos-crossfade.svg?style=for-the-badge
[hacs_custom]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[hacs]: https://github.com/custom-components/hacs

[ha-rest980-roomba]: https://github.com/jeremywillans/ha-rest980-roomba
[roomba-vacuum-card]: https://github.com/jeremywillans/lovelace-roomba-vacuum-card
[hass-addons]: https://github.com/jeremywillans/hass-addons
[event-emitter]: https://github.com/jeremywillans/event-emitter
[sonos-crossfade]: https://github.com/jeremywillans/sonos-crossfade
[BMC]: https://www.buymeacoffee.com/assets/img/custom_images/white_img.png