from adafruit_bitmap_font import bitmap_font

config = {

	################################
	# Meta API/Request Information #
	################################
    
	# Meta API
    'meta_api_url': 'https://graph.facebook.com/[pageId]?fields=id,name,fan_count&access_token=[accessToken]',
    

	# Number of retries per api fetch
	'meta_api_retries': 3,
    
	# How frequently we fetch new data from api
	'refresh_interval': 120,
    
	# Timeout threshold before retrying request
    'request_timeout': 5,

	#############################
	# Styling/Board Information #
	#############################
    
	# How fast text scrolls
	'scroll_speed': .75,
    
	# Hexcadecimal for color for title
	'title_color': 0xFFFFFF,
    
	# Hexadecimal for color of like 
	'like_color': 0xFFFFFF,
    
	# How wide the board is
	'matrix_width': 64,
    
	'font': bitmap_font.load_font('lib/5x7.bdf'),


	'text_padding': 2,
    

	'character_width': 4,
    'character_height': 6,
    'like_count_scale': 3,

	'min_label_characters': 3,
}