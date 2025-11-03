# Tasks: Fix Minimalistic Mode

**Input**: Design documents from `/specs/001-fix-minimalistic/`
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

**Purpose**: Ensure project is ready for minimalistic mode fix implementation

- [x] T001 Verify Python environment and dependencies are installed
- [x] T002 [P] Create test utility for minimalistic mode validation in src/test_minimalistic.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core investigation of current minimalistic mode issues

**⚠️ CRITICAL**: Complete investigation before implementing fixes

- [ ] T003 Analyze current minimalistic mode implementation in src/minimalistic_mode.py
- [ ] T004 Test current minimalistic mode output and identify issues
- [ ] T005 Analyze background detection method in src/minimalistic_mode.py
- [ ] T006 Analyze edge detection and enhancement in src/minimalistic_mode.py

**Checkpoint**: Issues understood - minimalistic mode fix implementation can now begin

---

## Phase 3: User Story 1 - Fix Minimalistic Mode Background and Edges (Priority: P1) 🔧

**Goal**: Implement proper background detection, set background to pure black with no characters, and emphasize subject edges without altering internal colors

**Independent Test**: Apply minimalistic mode and verify background is pure black with no characters, and subject edges are emphasized while internal colors remain unchanged

### Implementation for User Story 1

- [x] T007 [US1] Implement improved background detection using border sampling in src/minimalistic_mode.py
- [x] T008 [US1] Create background mask to prevent character rendering on background in src/minimalistic_mode.py
- [x] T009 [US1] Implement selective edge enhancement without altering internals in src/minimalistic_mode.py
- [x] T010 [US1] Update minimalistic processing pipeline in src/minimalistic_mode.py
- [x] T011 [US1] Test minimalistic mode background fix
- [x] T012 [US1] Test minimalistic mode edge enhancement

**Checkpoint**: At this point, User Story 1 should be fully functional and minimalistic mode should work correctly

---

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation updates

- [x] T013 Update quickstart.md with minimalistic mode fix validation steps
- [x] T014 Create minimalistic mode demo in notebooks/demo.ipynb
- [x] T015 Document minimalistic mode parameters

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
- Once investigation completes, minimalistic fix tasks can proceed

---

## Parallel Example: User Story 1

```bash
# Sequential investigation:
Task: "Analyze current minimalistic mode implementation in src/minimalistic_mode.py"
Task: "Test current minimalistic mode output and identify issues"

# Then parallel implementation:
Task: "Implement improved background detection using border sampling in src/minimalistic_mode.py"
Task: "Implement selective edge enhancement without altering internals in src/minimalistic_mode.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - understand the issues)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test minimalistic mode against requirements
5. Complete Phase 4: Basic polish for validation

### Incremental Delivery

1. Complete Setup + Foundational → Issues understood
2. Add User Story 1 → Test minimalistic mode independently → Deploy/Demo (Fixed!)
3. Future: Additional minimalistic features if needed

---

## Notes

- [P] tasks = different files, no dependencies
- [US1] label maps task to User Story 1 for traceability
- Each task includes exact file paths for implementation
- Focus on background detection and edge enhancement for minimalistic mode
- Validate with visual inspection and mask verification
- Commit after each task completion</content>
<parameter name="filePath">c:\Dev\ascii-g\specs\001-fix-minimalistic\tasks.md