# Implementation Plan: Fix Minimalistic Mode

**Branch**: `001-fix-minimalistic` | **Date**: November 3, 2025 | **Spec**: [link]
**Input**: Feature specification from `/specs/001-fix-minimalistic/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Fix minimalistic mode to properly detect background, set it to pure black with no characters, and emphasize subject edges without altering internal colors.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: Pillow (for image processing), OpenCV (for edge detection), NumPy (for calculations)  
**Storage**: N/A (image input/output only)  
**Testing**: Manual testing with background detection validation  
**Target Platform**: Cross-platform (Windows, macOS, Linux)  
**Project Type**: Modification to existing minimalistic_mode.py  
**Performance Goals**: Maintain processing under 30 seconds for standard images  
**Constraints**: Accurate background detection, edge enhancement without color alteration  
**Scale/Scope**: Single-user tool, small scale (no concurrent users, local processing)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

No specific gates defined in current constitution template. Assuming compliance with general principles (test-first, simplicity, etc.).

## Project Structure

### Documentation (this feature)

```text
specs/001-fix-minimalistic/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```text
src/
├── ascii_generator.py      # Main script (no changes needed)
├── image_processor.py      # Image loading (no changes)
├── ascii_renderer.py       # Core rendering (no changes)
└── minimalistic_mode.py    # MODIFY for background detection and edge enhancement
```

**Structure Decision**: Modify existing minimalistic_mode.py to improve background detection and edge processing.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [Modifying existing code] | [Fix requires changes to background detection logic] | [Creating separate module would duplicate edge detection code] |</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-minimalistic\plan.md