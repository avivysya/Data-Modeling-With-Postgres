# DROP TABLES

songplay_table_drop = "Drop table songplays"
user_table_drop = "Drop table users"
song_table_drop = "Drop table songs"
artist_table_drop = "Drop table artists"
time_table_drop = "Drop table time"

# CREATE TABLES

songplay_table_create = ("create table songplays ( songplay_id varchar, start_time bigint , user_id varchar , level varchar , song_id int , artist_id int , session_id int , location varchar, user_agent varchar)")

user_table_create = ("create table users (user_id varchar , first_name varchar, last_name varchar, gender varchar, level varchar )")

song_table_create = ("create table songs (song_id varchar , title varchar, artist_id varchar , year int , duration int )")

artist_table_create = ("create table artists (artist_id varchar , name varchar, location varchar, latitude varchar , longitude varchar )")

time_table_create = ("create table time (start_time timestamp, hour int , day int , week int, month int , year int , weekday varchar)")

# INSERT RECORDS

songplay_table_insert = (""" Insert into songplays (songplay_id,start_time,user_id,level,song_id,artist_id,session_id,location,user_agent)
values ( %s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = (""" Insert into users(user_id, first_name,last_name,gender,level)
VALUES ( %s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs ( song_id, title, artist_id, year, duration)
VALUES ( %s, %s, %s, %s, %s)
""")

artist_table_insert = (""" Insert into artists ( artist_id, name, location, latitude, longitude)
values (%s, %s, %s, %s, %s)
""")


time_table_insert = (""" Insert into time(start_time, hour,day,week,month,year,weekday)
values (%s, %s, %s, %s, %s, %s,%s)
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id song_id, artists.artist_id artist_id FROM songs JOIN artists ON (songs.artist_id = artists.artist_id) WHERE (songs.title = %s AND artists.name = %s AND songs.duration = %s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]