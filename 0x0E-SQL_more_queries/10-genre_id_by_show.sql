-- Lists all shows contained in hbtn_0d_tvshows that have atleast
-- one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows INNER JOIN tv_show_genres
INNER JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id &&
tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
