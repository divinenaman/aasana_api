query_dict = {
    "create_pose_table": """
        CREATE TABLE IF NOT EXISTS yoga_pose (
            id integer PRIMARY KEY,
            name text NOT NULL,
            desc text NOT NULL
        );
    """,

    "create_pose_tag_table": """
        CREATE TABLE IF NOT EXISTS yoga_pose_tag (
            id integer PRIMARY KEY,
            tag text NOT NULL,
            pose_id integer NOT NULL
        );
    """,
    "create_pose_landmark_angle_table": """
        CREATE TABLE IF NOT EXISTS pose_landmark_angle (
            id integer PRIMARY KEY,
            pose_id integer NOT NULL,
            landmark_1 integer NOT NULL,
            landmark_2 integer NOT NULL,
            intersection_landmark integer NOT NULL,
            min_value integer NOT NULL,
            max_value integer NOT NULL
        );
    """,

    "create_landmark_table": """
        CREATE TABLE IF NOT EXISTS landmark (
            id integer PRIMARY KEY,
            key text NOT NULL
        );
    """,
}
