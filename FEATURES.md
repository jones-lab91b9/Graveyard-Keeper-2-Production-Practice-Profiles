# Graveyard Keeper 2: Feature Scope

Status: Prerelease module plan. Checked 2026-09-05.

The items below are proposed capabilities. They are not release notes or a list of working features.

## Material budgets

Prepare a structure for local resource adjustments once the released game's item data can be verified.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Crafting experiments

Plan recipe-cost comparisons and test budgets without importing recipes from the first game.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Production pacing

Research whether individual production timers can be adjusted without damaging task progression.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Town development

Plan separate experiment profiles for town-restoration decisions.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Automation plans

Prepare a versioned reference for the announced production and undead-worker systems, with details deferred to release.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Progress snapshots

Investigate world and character save boundaries before offering a restoration workflow.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Shared application architecture

This theme is one adapter for a common application. The shared interface can manage profiles and show change previews; each game adapter must implement and validate its own behaviour. No universal memory addresses, item identifiers, save paths or hotkeys are supplied.

## Session scope

The proposed game-state assistance is scoped to the single-player game. Profile restoration must account for the complete relevant state, including any separate world and character data.

## First implementation target

After release, a player could compare two workshop plans and request a specific experiment budget. Until the recipes are verified, the package defines the workflow without inventing ingredients or costs.
