from igdb.wrapper import IGDBWrapper

wrapper = IGDBWrapper("1ucj7p9lz76qmng4s8xpcwoh0h69j5", "5qm7yknzijrnanrgy315m97mmq2esp")

class igdb_api:
    @classmethod
    def api_get_upcoming_games(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields id, name, cover.image_id; limit 25; where release_dates.date > {data} & platforms = {167, 169} & cover.image_id != null; sort release_dates.date asc;'
        )
        return byte_array

    @classmethod
    def api_get_game_by_marketplace(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, release_dates.human, release_dates.region, cover.image_id; limit 25; sort release_dates.date asc; where external_games.category = {data};'
        )
        return byte_array

    @classmethod
    def api_get_game_by_marketplace_extended(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, release_dates.human, release_dates.region, cover.image_id; limit 500; sort release_dates.date asc; where external_games.category = {data};'
        )
        return byte_array

    @classmethod
    def api_get_games_by_genre(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 25; where genres = {data} & platforms = {167, 169} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_genre_extended(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 500; where genres = {data} & platforms = {167, 169} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_platform(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 25; where platforms = {data} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_games_by_platform_extended(cls, data, time):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id; limit 500; where platforms = {data} & release_dates.date < {time} & cover.image_id != null; sort release_dates.date desc;'
        )
        return byte_array

    @classmethod
    def api_get_one_game(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'fields name, cover.image_id, genres.name, involved_companies.company.name, platforms.name, summary, game_modes.name; where id = {data};'
        )
        return byte_array

    @classmethod
    def api_search_game_by_name(cls, data):
        byte_array = wrapper.api_request(
            'games',
            f'search "{data}"; fields name, release_dates.human, release_dates.region, cover.image_id; limit 25;'
        )
        return byte_array