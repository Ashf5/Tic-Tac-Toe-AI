import sqlite3


def get_cursor():
    """
    This function returns a tuple with the connection object and the cursor object pointing towards the data.db database.
    """
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()     
    return (conn, cur)   

def reset():
    """
    This function resets the database.
    """
    cur = get_cursor()[1]
    cur.execute("DROP TABLE scores")
    cur.execute("CREATE TABLE scores (game_id INTEGER PRIMARY KEY AUTOINCREMENT, status INTEGER, played_as VARCHAR(1));")


def update(status, played_as):
    """
    This function takes as parameters status (-1, 0, 1) and played_as (x, o) and adds the game to the scores table.
    """
    conn, cur = get_cursor()
    cur.execute("INSERT INTO scores (status, played_as) VALUES (?, ?);", (status, played_as))
    conn.commit()

def fetch():
    """
    Returns a list of tuples with the values game_id, status, played_as. The list first displays the games played as "o" than the games played as "x". If it was not successful in fetching the scores it returns -1.
    """
    cur = get_cursor()[1]

    try:
        cur.execute("SELECT * FROM scores ORDER BY played_as;")
        scores = cur.fetchall()
    except:
        print("Error accessing database.")
        return -1

    return scores

def print_stats():
    data = fetch()
    stats_x = {0: 0, 1: 0, -1: 0}
    stats_o = {0: 0, 1: 0, -1: 0}

    for i in data:
        if i[2] == "o":
            stats_o[i[1]] += 1
            pass 
        else:
            stats_x[i[1]] += 1

    x = f"Playing as X you won {stats_x[1]} times, tied {stats_x[0]} times, and lost {stats_x[-1]} times."
    o = f"Playing as O you won {stats_o[1]} times, tied {stats_o[0]} times, and lost {stats_o[-1]} times."
    print(x)
    print(o)



