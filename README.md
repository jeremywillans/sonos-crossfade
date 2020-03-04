# Sonos Crossfade
## Custom Component For Home Assistant
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

This component creates a service `sonos_crossfade.update` that lets you change the crossfade setting on any one of your Sonos speakers. Requires the `sonos` component to be already setup.

## Install
1. Copy the `custom_components` forlder in your HA configuration folder (or install with [HACS](https://github.com/custom-components/hacs)).
2. Add
    ```
    sonos_crossfade:
    ```
    to the `configuration.yaml`

## Service Parameters
- `entity_id`: entity id of the speaker  (eg. `media_player.bedroom`)
- `enabled`: crossfade state.
