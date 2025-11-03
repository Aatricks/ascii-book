# Tasks: ASCII Art Generator

**Input**: Design documents from `/specs/001-ascii-art-generator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are not requested in the feature specification - focusing on implementation tasks only.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths follow the structure defined in plan.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 Initialize Python project with Pillow, OpenCV, NumPy dependencies
- [x] T003 [P] Configure basic project settings and requirements.txt

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create base image processing utilities in src/image_processor.py
- [x] T005 [P] Create ASCII character mapping constants in src/ascii_chars.py
- [x] T006 [P] Create base ASCII renderer class in src/ascii_renderer.py

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Generate High-Quality Colorized ASCII Art (Priority: P1) 🎯 MVP

**Goal**: Convert images to high-quality colorized ASCII art images with preserved details and color gradients

**Independent Test**: Upload an image and verify the output image displays ASCII characters with colors representing the original image details and gradients

### Implementation for User Story 1

- [x] T007 [US1] Implement image loading and validation in src/image_processor.py
- [x] T008 [US1] Implement luminance-based ASCII character mapping in src/ascii_renderer.py
- [x] T009 [US1] Implement color sampling and overlay in src/ascii_renderer.py
- [x] T010 [US1] Implement ASCII grid generation with high character density in src/ascii_renderer.py
- [x] T011 [US1] Implement image output rendering in src/ascii_renderer.py
- [x] T012 [US1] Create main CLI script in src/ascii_generator.py
- [x] T013 [US1] Integrate components in src/ascii_generator.py for end-to-end functionality

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Minimalistic Mode for Edge Emphasis (Priority: P2)

**Goal**: Provide a minimalistic mode that sets the background to pure black pixels and emphasizes character edges without altering internal character colors or detecting edges within the character.

**Independent Test**: Apply minimalistic mode to an image with a subject on a background and verify the background becomes black and edges are emphasized without internal alterations.

### Implementation for User Story 2

- [x] T017 [US2] Create minimalistic mode module in src/minimalistic_mode.py
- [x] T018 [US2] Implement edge detection using OpenCV Canny algorithm in src/minimalistic_mode.py
- [x] T019 [US2] Implement background removal to pure black pixels in src/minimalistic_mode.py
- [x] T020 [US2] Implement edge emphasis without altering internal character colors in src/minimalistic_mode.py
- [x] T021 [US2] Add --minimalistic CLI option parsing in src/ascii_generator.py
- [x] T022 [US2] Integrate minimalistic mode into processing pipeline in src/ascii_generator.py

**Checkpoint**: At this point, User Story 2 should be fully functional and testable independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Basic improvements for MVP readiness

- [x] T014 Create demo Jupyter notebook in notebooks/demo.ipynb
- [x] T015 Update quickstart.md with working examples
- [x] T016 Basic error handling and user feedback improvements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on User Story 1 completion (User Story 2 can be added independently)

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models/utilities before core logic
- Core implementation before integration
- Story complete before moving to polish

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Story 1 tasks can proceed
- Once Foundational phase completes, User Story 2 tasks can proceed in parallel with User Story 1

---

## Parallel Example: User Story 1

```bash
# Launch foundational components together:
Task: "Create ASCII character mapping constants in src/ascii_chars.py"
Task: "Create base ASCII renderer class in src/ascii_renderer.py"

# Then proceed with implementation tasks sequentially
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Complete Phase 4: Basic polish for MVP readiness
6. Deploy/demo MVP

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Enhanced product
4. Future: Additional features as next increments

---

## Notes

- [P] tasks = different files, no dependencies
- [US1] label maps task to User Story 1 for traceability
- Each task includes exact file paths for implementation
- MVP focuses on core ASCII art generation functionality
- Verify functionality after each major component
- Commit after each task completion