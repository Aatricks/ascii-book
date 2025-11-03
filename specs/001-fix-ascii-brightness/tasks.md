# Tasks: Fix ASCII Brightness and Colors

**Input**: Design documents from `/specs/001-fix-ascii-brightness/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are not requested in the feature specification - focusing on implementation tasks only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description` with file path

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow the structure defined in plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Ensure project is ready for brightness fix implementation

- [x] T001 Verify Python environment and dependencies are installed
- [x] T002 [P] Create test script for brightness comparison in src/test_brightness.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core investigation and understanding of current brightness issue

**⚠️ CRITICAL**: Complete investigation before implementing fixes

- [x] T003 Analyze current luminance calculation in src/ascii_renderer.py
- [x] T004 Analyze current color sampling method in src/ascii_renderer.py
- [x] T005 Create brightness measurement utility in src/brightness_utils.py
- [x] T006 Test current brightness levels against original images

**Checkpoint**: Issue understood - brightness fix implementation can now begin

---

## Phase 3: User Story 1 - Fix Brightness and Color Accuracy (Priority: P1) 🔧

**Goal**: Implement gamma-corrected luminance and area-averaged color sampling to match original image brightness and colors

**Independent Test**: Compare mean color levels between original image and ASCII output, verify brightness difference < 10%

### Implementation for User Story 1

- [x] T007 [US1] Implement gamma-corrected luminance calculation in src/ascii_renderer.py
- [x] T008 [US1] Implement area-averaged color sampling in src/ascii_renderer.py
- [x] T009 [US1] Add brightness calibration factor in src/ascii_renderer.py
- [x] T010 [US1] Update ASCIIGenerator class to use corrected calculations
- [x] T011 [US1] Test brightness fix with sample images
- [x] T012 [US1] Validate color accuracy improvements

**Checkpoint**: At this point, User Story 1 should be fully functional and brightness/colors should match original within tolerance

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation updates

- [x] T013 Update quickstart.md with brightness fix validation steps
- [x] T014 Create brightness comparison demo in notebooks/demo.ipynb
- [x] T015 Document brightness calibration parameters

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS User Story 1
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on User Story 1 completion

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Investigation before implementation
- Core fixes before validation
- Story complete before moving to polish

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- Foundational analysis tasks can run sequentially
- Once investigation completes, brightness fix tasks can proceed

---

## Parallel Example: User Story 1

```bash
# Sequential investigation:
Task: "Analyze current luminance calculation in src/ascii_renderer.py"
Task: "Analyze current color sampling method in src/ascii_renderer.py"

# Then parallel implementation:
Task: "Implement gamma-corrected luminance calculation in src/ascii_renderer.py"
Task: "Implement area-averaged color sampling in src/ascii_renderer.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - understand the issue)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test brightness accuracy against original images
5. Complete Phase 4: Basic polish for validation

### Incremental Delivery

1. Complete Setup + Foundational → Issue understood
2. Add User Story 1 → Test brightness fix independently → Deploy/Demo (Fixed!)
3. Future: Additional calibration features if needed

---

## Notes

- [P] tasks = different files, no dependencies
- [US1] label maps task to User Story 1 for traceability
- Each task includes exact file paths for implementation
- Focus on gamma correction and color averaging for brightness accuracy
- Validate with mean color level comparison
- Commit after each task completion</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-ascii-brightness\tasks.md