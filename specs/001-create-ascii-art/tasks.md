# Tasks: ASCII Art Generator

**Input**: Design documents from `/specs/001-create-ascii-art/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [x] T001 Create the basic directory structure: `src/ascii_art_generator/` and `tests/`.
- [x] T002 [P] Create an initial `pyproject.toml` with `Pillow`, `numpy`, and `opencv-python` as dependencies.
- [x] T003 [P] Create a `.gitignore` file with standard Python ignores.
- [x] T004 [P] Create a basic `README.md` with the project title and a brief description.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [x] T005 Implement the basic CLI argument parsing in `src/ascii_art_generator/main.py` using `argparse`.
- [x] T006 In `src/ascii_art_generator/conversion.py`, create a function to load an image from a file path using Pillow.
- [x] T007 In `src/ascii_art_generator/conversion.py`, create a function to resize an image based on a given width, maintaining aspect ratio.

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Standard Conversion (Priority: P1) 🎯 MVP

**Goal**: Convert a standard image to colorized ASCII art.

**Independent Test**: Run the tool with an input image and verify the output is a recognizable, colorized ASCII art image.

### Implementation for User Story 1

- [x] T008 [US1] In `src/ascii_art_generator/conversion.py`, implement a function to convert a resized image to grayscale.
- [x] T009 [US1] In `src/ascii_art_generator/conversion.py`, define a mapping from grayscale values to a set of ASCII characters.
- [x] T010 [US1] In `src/ascii_art_generator/conversion.py`, implement the main conversion function that iterates over the image, selects ASCII characters based on brightness, and gets the original color.
- [x] T011 [US1] In `src/ascii_art_generator/conversion.py`, create a function to draw the colorized ASCII characters onto a new image canvas.
- [x] T012 [US1] In `src/ascii_art_generator/main.py`, integrate the conversion functions and save the final image to the specified output path.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Minimalistic Mode (Priority: P2)

**Goal**: Create a "sticker" effect by isolating a subject and enhancing its outline.

**Independent Test**: Run the tool with the `--minimalistic` flag and verify the output has a black background and an enhanced subject.

### Implementation for User Story 2

- [x] T013 [US2] In `src/ascii_art_generator/minimalistic.py`, implement a simple color-based segmentation function to create a background mask.
- [x] T014 [US2] In `src/ascii_art_generator/minimalistic.py`, implement an edge detection function (e.g., using OpenCV's Canny or Sobel filters) to find the subject's outline from the mask.
- [x] T015 [US2] In `src/ascii_art_generator/conversion.py`, modify the main conversion loop to handle the minimalistic mode: if a pixel is in the background mask, render a black space; if it's on the edge, use a brighter character.
- [x] T016 [US2] In `src/ascii_art_generator/main.py`, add the logic to call the minimalistic mode functions when the `--minimalistic` flag is present.
- [x] T017 [US2] [P] Research and prototype the ML-based background removal method. This is a larger task and can be broken down further.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories.

- [x] T018 [P] Write unit tests for the core conversion logic in `tests/test_conversion.py`.
- [x] T019 [P] Write unit tests for the minimalistic mode logic in `tests/test_minimalistic.py`.
- [x] T020 [P] Update the `README.md` with detailed usage instructions and examples.
- [x] T021 Add error handling for file I/O and invalid image formats in `src/ascii_art_generator/main.py`.
- [x] T022 Refine the ASCII character mapping and colorization for better visual quality.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed before all other phases.
- **Foundational (Phase 2)** must be completed before User Story implementation.
- **User Story 1 (Phase 3)** can be implemented after the Foundational phase.
- **User Story 2 (Phase 4)** can be implemented after the Foundational phase. It has a dependency on the conversion logic from User Story 1.
- **Polish (Phase 5)** can be done after the user stories are complete.

## Parallel Opportunities

- Within Phase 1, T002, T003, and T004 can be done in parallel.
- After Phase 2, work on User Story 1 and User Story 2 could potentially be parallelized, but since US2 depends on US1's conversion logic, it's better to do them sequentially.
- Within Phase 5, the testing and documentation tasks (T018, T019, T020) can be done in parallel.
