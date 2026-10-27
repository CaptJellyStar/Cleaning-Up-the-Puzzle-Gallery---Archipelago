import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

PIECES_CSV = BASE_DIR / "pieces.csv"
PIECE_LOCATIONS_CSV = BASE_DIR / "piece_location.csv"
PUZZLES_CSV = BASE_DIR / "puzzles.csv"

LARGE_PIECE_LOCATIONS_CSV = BASE_DIR / "large_piece_location.csv"
LARGE_PUZZLES_CSV = BASE_DIR / "large_puzzles.csv"


# These are the four tutorial puzzles for the original map
TUTORIAL_PUZZLE_IDS = {
    "klimt_beech_grove_i",
    "hokusai_kajikazawa_kai",
    "vangogh_self_portrait_1889",
    "mondrian_composition_gray_brown",
}

# These are the four tutorial puzzles for the large map
LARGE_TUTORIAL_PUZZLE_IDS = {
    "tut_the_kiss",
    "tut_starry_night",
    "tut_great_wave",
    "tut_girl_reading_letter",
}


def read_csv(path):
    """Read a CSV file and ignore the first/header line."""

    with path.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.reader(
            file,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            doublequote=True
        )

        # Ignore the header.
        header = next(reader, None)

        if header is None:
            raise ValueError(f"{path.name} is empty.")

        print(f"{path.name} header: {header}")

        return list(reader)


def validate_pieces(rows):
    print()
    print("========================================")
    print("VALIDATING pieces.csv")
    print("========================================")

    if not rows:
        raise ValueError("pieces.csv is empty.")

    print(f"Total rows: {len(rows)}")

    expected_count = 2034

    if len(rows) != expected_count:
        raise ValueError(
            f"Expected {expected_count} piece items, "
            f"but found {len(rows)}."
        )

    seen_ap_names = set()
    seen_game_ids = set()

    for row_number, row in enumerate(rows, start=1):
        if len(row) != 4:
            raise ValueError(
                f"pieces.csv row {row_number} has "
                f"{len(row)} columns instead of 4."
            )

        ap_name, game_piece_id, puzzle_id, puzzle_name = row

        if ap_name in seen_ap_names:
            raise ValueError(
                f"Duplicate AP Piece name: {ap_name}"
            )

        if game_piece_id in seen_game_ids:
            raise ValueError(
                f"Duplicate Game Piece ID: {game_piece_id}"
            )

        if puzzle_id in TUTORIAL_PUZZLE_IDS:
            raise ValueError(
                f"Tutorial piece found in pieces.csv: "
                f"{game_piece_id}"
            )

        seen_ap_names.add(ap_name)
        seen_game_ids.add(game_piece_id)

    print("Piece count: PASSED")
    print("Duplicate AP names: PASSED")
    print("Duplicate Game Piece IDs: PASSED")
    print("Tutorial pieces excluded: PASSED")


def validate_piece_locations(rows):
    print()
    print("========================================")
    print("VALIDATING piece_location.csv")
    print("========================================")

    if not rows:
        raise ValueError("piece_location.csv is empty.")

    print(f"Total rows: {len(rows)}")

    expected_count = 2071

    if len(rows) != expected_count:
        raise ValueError(
            f"Expected {expected_count} piece locations, "
            f"but found {len(rows)}."
        )

    seen_ap_names = set()
    seen_game_ids = set()

    for row_number, row in enumerate(rows, start=1):
        if len(row) != 4:
            raise ValueError(
                f"piece_location.csv row {row_number} has "
                f"{len(row)} columns instead of 4."
            )

        ap_name, game_piece_id, puzzle_id, puzzle_name = row

        if ap_name in seen_ap_names:
            raise ValueError(
                f"Duplicate AP Piece name: {ap_name}"
            )

        if game_piece_id in seen_game_ids:
            raise ValueError(
                f"Duplicate Game Piece ID: {game_piece_id}"
            )

        seen_ap_names.add(ap_name)
        seen_game_ids.add(game_piece_id)

    tutorial_count = sum(
        1
        for row in rows
        if row[2] in TUTORIAL_PUZZLE_IDS
    )

    if tutorial_count != 37:
        raise ValueError(
            f"Expected 37 tutorial piece locations, "
            f"but found {tutorial_count}."
        )

    print("Piece location count: PASSED")
    print("Duplicate AP names: PASSED")
    print("Duplicate Game Piece IDs: PASSED")
    print(
        f"Tutorial piece locations: "
        f"{tutorial_count} — PASSED"
    )


def validate_puzzles(rows):
    print()
    print("========================================")
    print("VALIDATING puzzles.csv")
    print("========================================")

    if not rows:
        raise ValueError("puzzles.csv is empty.")

    print(f"Total rows: {len(rows)}")

    expected_count = 87

    if len(rows) != expected_count:
        raise ValueError(
            f"Expected {expected_count} puzzles, "
            f"but found {len(rows)}."
        )

    seen_ap_names = set()
    seen_game_ids = set()

    for row_number, row in enumerate(rows, start=1):
        if len(row) != 8:
            raise ValueError(
                f"puzzles.csv row {row_number} has "
                f"{len(row)} columns instead of 8."
            )

        (
            ap_name,
            game_puzzle_id,
            puzzle_name,
            artist,
            year,
            columns,
            rows_count,
            piece_count,
        ) = row

        if ap_name in seen_ap_names:
            raise ValueError(
                f"Duplicate AP Puzzle name: {ap_name}"
            )

        if game_puzzle_id in seen_game_ids:
            raise ValueError(
                f"Duplicate Game Puzzle ID: {game_puzzle_id}"
            )

        seen_ap_names.add(ap_name)
        seen_game_ids.add(game_puzzle_id)

    tutorial_count = sum(
        1
        for row in rows
        if row[1] in TUTORIAL_PUZZLE_IDS
    )

    if tutorial_count != 4:
        raise ValueError(
            f"Expected 4 tutorial puzzles, "
            f"but found {tutorial_count}."
        )

    ap_count = len(rows) - tutorial_count

    if ap_count != 83:
        raise ValueError(
            f"Expected 83 AP puzzle locations, "
            f"but calculated {ap_count}."
        )

    print("Puzzle count: PASSED")
    print("Duplicate AP names: PASSED")
    print("Duplicate Game Puzzle IDs: PASSED")
    print(
        f"Tutorial puzzles: "
        f"{tutorial_count} — PASSED"
    )
    print(
        f"AP puzzle locations: "
        f"{ap_count} — PASSED"
    )

def validate_large_piece_locations(rows):
    print()
    print("========================================")
    print("VALIDATING large_piece_location.csv")
    print("========================================")

    if not rows:
        raise ValueError("large_piece_location.csv is empty.")

    print(f"Total rows: {len(rows)}")

    expected_count = 3800

    if len(rows) != expected_count:
        raise ValueError(
            f"Expected {expected_count} Large Gallery piece locations, "
            f"but found {len(rows)}."
        )

    seen_ap_names = set()
    seen_game_ids = set()

    for row_number, row in enumerate(rows, start=1):
        if len(row) != 4:
            raise ValueError(
                f"large_piece_location.csv row {row_number} has "
                f"{len(row)} columns instead of 4."
            )

        ap_name, game_piece_id, puzzle_id, puzzle_name = row

        if ap_name in seen_ap_names:
            raise ValueError(
                f"Duplicate Large AP Piece name: {ap_name}"
            )

        if game_piece_id in seen_game_ids:
            raise ValueError(
                f"Duplicate Large Game Piece ID: {game_piece_id}"
            )

        seen_ap_names.add(ap_name)
        seen_game_ids.add(game_piece_id)

    tutorial_count = sum(
        1
        for row in rows
        if row[2] in LARGE_TUTORIAL_PUZZLE_IDS
    )

    if tutorial_count != 39:
        raise ValueError(
            f"Expected 39 Large Gallery tutorial piece locations, "
            f"but found {tutorial_count}."
        )

    ap_count = len(rows) - tutorial_count

    if ap_count != 3761:
        raise ValueError(
            f"Expected 3761 Large Gallery AP pieces, "
            f"but calculated {ap_count}."
        )

    print("Large piece location count: PASSED")
    print("Duplicate AP names: PASSED")
    print("Duplicate Game Piece IDs: PASSED")
    print(
        f"Large tutorial piece locations: "
        f"{tutorial_count} — PASSED"
    )
    print(
        f"Large AP pieces: "
        f"{ap_count} — PASSED"
    )


def validate_large_puzzles(rows):
    print()
    print("========================================")
    print("VALIDATING large_puzzles.csv")
    print("========================================")

    if not rows:
        raise ValueError("large_puzzles.csv is empty.")

    print(f"Total rows: {len(rows)}")

    expected_count = 110

    if len(rows) != expected_count:
        raise ValueError(
            f"Expected {expected_count} Large Gallery puzzles, "
            f"but found {len(rows)}."
        )

    seen_ap_names = set()
    seen_game_ids = set()

    for row_number, row in enumerate(rows, start=1):
        if len(row) != 8:
            raise ValueError(
                f"large_puzzles.csv row {row_number} has "
                f"{len(row)} columns instead of 8."
            )

        (
            ap_name,
            game_puzzle_id,
            puzzle_name,
            artist,
            year,
            columns,
            rows_count,
            piece_count,
        ) = row

        if ap_name in seen_ap_names:
            raise ValueError(
                f"Duplicate Large AP Puzzle name: {ap_name}"
            )

        if game_puzzle_id in seen_game_ids:
            raise ValueError(
                f"Duplicate Large Game Puzzle ID: {game_puzzle_id}"
            )

        seen_ap_names.add(ap_name)
        seen_game_ids.add(game_puzzle_id)

    tutorial_count = sum(
        1
        for row in rows
        if row[1] in LARGE_TUTORIAL_PUZZLE_IDS
    )

    if tutorial_count != 4:
        raise ValueError(
            f"Expected 4 Large Gallery tutorial puzzles, "
            f"but found {tutorial_count}."
        )

    ap_count = len(rows) - tutorial_count

    if ap_count != 106:
        raise ValueError(
            f"Expected 106 Large Gallery AP puzzle locations, "
            f"but calculated {ap_count}."
        )

    print("Large puzzle count: PASSED")
    print("Duplicate AP names: PASSED")
    print("Duplicate Game Puzzle IDs: PASSED")
    print(
        f"Large tutorial puzzles: "
        f"{tutorial_count} — PASSED"
    )
    print(
        f"Large AP puzzle locations: "
        f"{ap_count} — PASSED"
    )

def generate_gallery_data(pieces, piece_locations, puzzles, large_piece_locations, large_puzzles):

    """Generate GalleryData.py from the validated CSV data."""

    output_path = Path(__file__).parent / "GalleryData.py"

    with output_path.open(
        "w",
        encoding="utf-8",
        newline=""
    ) as file:

        file.write(
            '"""'
            '\nGenerated from pieces.csv, piece_location.csv, and puzzles.csv.'
            '\nDO NOT EDIT THIS FILE MANUALLY.'
            '\n"""'
            '\n\n'
        )

        file.write(
            "TUTORIAL_PUZZLE_IDS = {\n"
            "    'klimt_beech_grove_i',\n"
            "    'hokusai_kajikazawa_kai',\n"
            "    'vangogh_self_portrait_1889',\n"
            "    'mondrian_composition_gray_brown',\n"
            "}\n\n"
        )

        file.write(
            "LARGE_TUTORIAL_PUZZLE_IDS = {\n"
            "    'tut_the_kiss',\n"
            "    'tut_starry_night',\n"
            "    'tut_great_wave',\n"
            "    'tut_girl_reading_letter',\n"
            "}\n\n"
        )

        # --------------------------------------------------
        # Piece items
        # --------------------------------------------------

        file.write("PIECE_ITEMS = {\n")

        for row in pieces:
            ap_name = row[0]
            game_piece_id = row[1]
            game_puzzle_id = row[2]
            puzzle_name = row[3]

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_piece_id': {game_piece_id!r},\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'puzzle_name': {puzzle_name!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Large Gallery piece items
        # --------------------------------------------------

        file.write("LARGE_PIECE_ITEMS = {\n")

        for row in large_piece_locations:
            ap_name = row[0]
            game_piece_id = row[1]
            game_puzzle_id = row[2]
            puzzle_name = row[3]

            # Tutorial pieces are available from the beginning
            # and are not Archipelago items.
            if game_puzzle_id in LARGE_TUTORIAL_PUZZLE_IDS:
                continue

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_piece_id': {game_piece_id!r},\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'puzzle_name': {puzzle_name!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Piece locations
        # --------------------------------------------------

        file.write("PIECE_LOCATIONS = {\n")

        for row in piece_locations:
            ap_name = row[0]
            game_piece_id = row[1]
            game_puzzle_id = row[2]
            puzzle_name = row[3]

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_piece_id': {game_piece_id!r},\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'puzzle_name': {puzzle_name!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Large Gallery piece locations
        # --------------------------------------------------

        file.write("LARGE_PIECE_LOCATIONS = {\n")

        for row in large_piece_locations:
            ap_name = row[0]
            game_piece_id = row[1]
            game_puzzle_id = row[2]
            puzzle_name = row[3]

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_piece_id': {game_piece_id!r},\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'puzzle_name': {puzzle_name!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Puzzles
        # --------------------------------------------------

        file.write("PUZZLES = {\n")

        for row in puzzles:
            ap_name = row[0]
            game_puzzle_id = row[1]
            title = row[2]
            artist = row[3]
            year = row[4]
            columns = row[5]
            rows = row[6]
            piece_count = row[7]

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'title': {title!r},\n"
                f"        'artist': {artist!r},\n"
                f"        'year': {year!r},\n"
                f"        'columns': {columns!r},\n"
                f"        'rows': {rows!r},\n"
                f"        'piece_count': {piece_count!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Large Gallery puzzles
        # --------------------------------------------------

        file.write("LARGE_PUZZLES = {\n")

        for row in large_puzzles:
            ap_name = row[0]
            game_puzzle_id = row[1]
            title = row[2]
            artist = row[3]
            year = row[4]
            columns = row[5]
            rows = row[6]
            piece_count = row[7]

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'title': {title!r},\n"
                f"        'artist': {artist!r},\n"
                f"        'year': {year!r},\n"
                f"        'columns': {columns!r},\n"
                f"        'rows': {rows!r},\n"
                f"        'piece_count': {piece_count!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Puzzle bundle items
        # --------------------------------------------------

        file.write("PUZZLE_ITEMS = {\n")

        for row in puzzles:
            ap_name = row[0]
            game_puzzle_id = row[1]
            title = row[2]
            piece_count = row[7]

            # Tutorial puzzles are not Archipelago items.
            if game_puzzle_id in TUTORIAL_PUZZLE_IDS:
                continue

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'title': {title!r},\n"
                f"        'piece_count': {piece_count!r},\n"
                f"    }},\n"
            )

        file.write("}\n\n")

        # --------------------------------------------------
        # Large Gallery puzzle bundle items
        # --------------------------------------------------

        file.write("LARGE_PUZZLE_ITEMS = {\n")

        for row in large_puzzles:
            ap_name = row[0]
            game_puzzle_id = row[1]
            title = row[2]
            piece_count = row[7]

            # Tutorial puzzles are not Archipelago items.
            if game_puzzle_id in LARGE_TUTORIAL_PUZZLE_IDS:
                continue

            file.write(
                f"    {ap_name!r}: {{\n"
                f"        'game_puzzle_id': {game_puzzle_id!r},\n"
                f"        'title': {title!r},\n"
                f"        'piece_count': {piece_count!r},\n"
                f"    }},\n"
            )

        file.write("}\n")

    print()
    print("========================================")
    print("GENERATED GalleryData.py")
    print("========================================")
    print(f"Output: {output_path}")
    print(f"Piece items: {len(pieces)}")
    print(f"Piece locations: {len(piece_locations)}")
    print(f"Puzzles: {len(puzzles)}")

    puzzle_item_count = sum(
        1
        for row in puzzles
        if row[1] not in TUTORIAL_PUZZLE_IDS
    )

    print(f"Puzzle bundle items: {puzzle_item_count}")
    print("========================================")


def main():
    print("========================================")
    print("Cleaning Up the Puzzle Gallery")
    print("Gallery Data Validator")
    print("========================================")

    pieces = read_csv(PIECES_CSV)
    piece_locations = read_csv(PIECE_LOCATIONS_CSV)
    puzzles = read_csv(PUZZLES_CSV)

    large_piece_locations = read_csv(LARGE_PIECE_LOCATIONS_CSV)
    large_puzzles = read_csv(LARGE_PUZZLES_CSV)

    validate_pieces(pieces)
    validate_piece_locations(piece_locations)
    validate_puzzles(puzzles)

    validate_large_piece_locations(large_piece_locations)
    validate_large_puzzles(large_puzzles)

    print()
    print("========================================")
    print("VALIDATION COMPLETE")
    print("========================================")
    print("All CSV files passed validation.")
    print()
    print("Expected Main Gallery data:")
    print(f"  Puzzle locations: {83}")
    print(f"  Piece items:      {2034}")
    print(f"  Piece locations:  {2071}")
    print(f"  Tutorial pieces:  {37}")

    print()
    print("Expected Large Gallery data:")
    print(f"  Puzzle locations: {106}")
    print(f"  Piece items:      {3761}")
    print(f"  Piece locations:  {3800}")
    print(f"  Tutorial pieces:  {39}")
    print("========================================")

    generate_gallery_data(
        pieces,
        piece_locations,
        puzzles,
        large_piece_locations,
        large_puzzles
    )

if __name__ == "__main__":
    main()