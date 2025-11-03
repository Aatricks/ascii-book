# Implementation Plan: Fix ASCII Brightness and Colors

**Branch**: `001-fix-ascii-brightness` | **Date**: November 3, 2025 | **Spec**: [link]
**Input**: Feature specification from `/specs/001-fix-ascii-brightness/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Fix brightness and color accuracy issues in ASCII art generation where output is overly bright and colors don't match the original image. Test by comparing mean color levels.

## Technical Context

**Language/Version**: Python 3.12  
**Primary Dependencies**: Pillow (for image processing), OpenCV (for edge detection in minimalistic mode), NumPy (for calculations)  
**Storage**: N/A (image input/output only)  
**Testing**: Manual testing with brightness comparison  
**Target Platform**: Cross-platform (Windows, macOS, Linux)  
**Project Type**: Modification to existing Python application  
**Performance Goals**: Maintain processing under 30 seconds for standard images  
**Constraints**: Fix brightness accuracy without degrading detail preservation or color gradients  
**Scale/Scope**: Single-user tool, small scale (no concurrent users, local processing)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

No specific gates defined in current constitution template. Assuming compliance with general principles (test-first, simplicity, etc.).

## Project Structure

### Documentation (this feature)

```text
specs/001-fix-ascii-brightness/
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
├── ascii_renderer.py       # Core rendering - MODIFY for brightness fix
└── minimalistic_mode.py    # Edge detection (no changes)
```

**Structure Decision**: Modify existing ascii_renderer.py to fix brightness calculation and color mapping.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [Modifying existing code] | [Fix requires changes to core rendering logic] | [Creating separate module would duplicate code and complicate maintenance] |</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-ascii-brightness\plan.md