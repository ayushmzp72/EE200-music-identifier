from collections import Counter

def match_song(
    query_hashes,
    database
):

    best_song = None
    best_score = 0
    MIN_MATCH_SCORE = 1
    best_offsets = []

    for song_name, db_hashes in database.items():

        offsets = []

        for q_sig, q_time in query_hashes:

            for db_sig, db_time in db_hashes:

                if q_sig == db_sig:

                    offsets.append(
                        round(
                            db_time - q_time,
                            2
                        )
                    )

        if len(offsets) == 0:
            continue

        offset_counter = Counter(offsets)

        score = max(
            offset_counter.values()
        )

        if score > best_score:

            best_score = score
            best_song = song_name
            best_offsets = offsets

        if score < MIN_MATCH_SCORE:
            return None, []

    return best_song, best_offsets