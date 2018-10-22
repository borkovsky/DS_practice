#counting nulls
 SELECT ds,
	COUNT(DISTINCT(post_id)) AS cnt_posts,
	COUNT(DISTINCT IF(num_likes > 0, post_id, NULL)) AS cnt_posts_likes
 FROM post_likes
 GROUP BY ds;