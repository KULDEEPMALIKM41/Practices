from covid import Covid
from datetime import datetime as dt

def covidUpdatesWorldWide():
	worldwide_total_active_cases = Covid().get_total_active_cases()
	worldwide_total_confirmed_cases = Covid().get_total_confirmed_cases()
	worldwide_total_recovered = Covid().get_total_recovered()
	worldwide_total_deaths = Covid().get_total_deaths()

	print('\nWORLDWIDE COVID INFORMATION\n')
	print('TOTAL ACTIVE     :    '+str(worldwide_total_active_cases))
	print('TOTAL CONFIRMED  :    '+str(worldwide_total_confirmed_cases))
	print('TOTAL RECOVERED  :    '+str(worldwide_total_recovered))
	print('TOTAL DEATHS     :    '+str(worldwide_total_deaths))

def covidUpdatesSpecificCountry(i_country):
	specific_country_covid_info = Covid().get_status_by_country_name(i_country)

	country_total_active_cases = specific_country_covid_info['active']
	country_total_confirmed_cases = specific_country_covid_info['confirmed']
	country_total_recovered = specific_country_covid_info['recovered']
	country_total_deaths = specific_country_covid_info['deaths']
	updatd_time_epoch = specific_country_covid_info['last_update']
	date_updated_at = dt.fromtimestamp(updatd_time_epoch/1000)

	print('\n' + i_country +' COVID INFORMATION\n')
	print('TOTAL ACTIVE     :    '+str(country_total_active_cases))
	print('TOTAL CONFIRMED  :    '+str(country_total_confirmed_cases))
	print('TOTAL RECOVERED  :    '+str(country_total_recovered))
	print('TOTAL DEATHS     :    '+str(country_total_deaths))
	print('LAST UPDATE AT   :    '+str(date_updated_at))

if __name__ == '__main__':
	covidUpdatesWorldWide()
	while True:
		country = input("\n\nENTER THE COUNTRY'S FULL NAME : ")
		try:
			covidUpdatesSpecificCountry(country)
			break
		except:
			print('COUNTRY NAME IS NOT VALID!')
			country_list = input("\n\nDO YOU WANT TO SEE COUNTRY LIST (y/n) : ")
			if country_list == 'y':
				country_list = Covid().list_countries()
				for country in country_list:
					print(country['name'])
