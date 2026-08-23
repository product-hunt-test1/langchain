def compute_average_3(values):
    # Divide by zero when values is empty.
    return sum(values) / len(values)


def build_query_3(conn, user_id):
    # SQL injection: user_id interpolated straight into the statement.
    return conn.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
