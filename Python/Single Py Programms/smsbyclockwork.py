from clockwork import clockwork
import time

api=clockwork.API('d3954d460c539802fb36dcdae011e33cecb320cf')

message=clockwork.SMS(to='918818919146',message='hello friend')

response=api.send(message)

if response.success:
	print(response.id)
else:
	print(response.error_code)
	print(response.error_message)