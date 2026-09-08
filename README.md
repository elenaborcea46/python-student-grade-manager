# Python Student Grade Manager

A console application for managing students, disciplines and grades, developed in Python using a layered architecture.

## Features

- Add, update, delete and list students
- Search students by name
- Add, update, delete and list disciplines
- Search disciplines by professor
- Assign grades to students
- Display a student's grades
- Display all grades for a discipline
- Generate students randomly
- Rank students by their results for a discipline
- Display the top 20% of students by average grade
- Generate discipline and student statistics
- Store application data in text files
- Validate input and handle application errors

## Architecture

The application follows a layered structure:

- `Domain` – domain entities and validators
- `Repos` – in-memory and file-based repositories
- `Services` – business logic and statistics
- `UI` – console interface and application coordination
- `Utils` – utility functions
- `Tests` – automated tests
- `data` – persistent application data

## Technologies and concepts

- Python
- Object-oriented programming
- Layered architecture
- Repository pattern
- File persistence
- Input validation
- Exception handling
- Sorting and statistical operations
- Unit testing

## Running the application

1. Install Python 3.
2. Clone the repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python main.py