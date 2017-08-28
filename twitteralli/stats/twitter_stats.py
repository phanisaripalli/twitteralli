from django.db import connection

def get_overview():
    with connection.cursor() as cursor:
        cursor.execute("SELECT search_key, count(*) as total_tweets, "
                       "count(distinct(user_id)) as distinct_users, "
                       "min(recorded_at)::text as min_recorded " 
                       "FROM twitter.tweet "                        
                       "WHERE 1 = 1 AND (recorded_at >= (now() - interval '10 minute')) "   
                       "GROUP BY search_key "
                       "ORDER BY total_tweets DESC "
                       "LIMIT 1")
        row = cursor.fetchone()
        cursor.close()

    return row


def poular_hashtags():
    with connection.cursor() as cursor:
        cursor.execute("SELECT hashtag , COUNT(*) as count "
                       "FROM twitter.tweet_hashtag th "
                       "JOIN twitter.tweet t on t.id = th.tweet_id "
                       "WHERE recorded_at >= current_timestamp - interval '10 minutes' " 
                       "GROUP BY hashtag "
                       "ORDER BY count DESC "
                       "LIMIT 10")
        row = cursor.fetchall()
    return row

def minutly_dsitribution():
    with connection.cursor() as cursor:
        cursor.execute("SELECT to_char(recorded_at, 'HH24:MI') as hr_min, count(*) as total_tweets "
                       "FROM twitter.tweet  "
                       "WHERE 1 = 1 AND recorded_at >= current_timestamp - interval '10 minute' "
                       "GROUP BY hr_min "
                       "ORDER BY hr_min ")
        row = cursor.fetchall()
    return row

def avg_distribution():
    with connection.cursor() as cursor:
        cursor.execute("SELECT AVG(total_tweets)::INT AS avg_tweets "
                       "FROM ( "  
                       "SELECT to_char(recorded_at, 'HH24:MI') as hr_min, count(*) as total_tweets "
                       "FROM twitter.tweet  "
                       "WHERE 1 = 1 AND recorded_at >= current_timestamp - interval '10 minute' "
                       "GROUP BY hr_min "
                       "ORDER BY hr_min "
                       ") sq")
        row = cursor.fetchone()
    return row

