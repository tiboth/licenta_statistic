import datetime as DT

from repository.AdvertisementRepository import AdvertisementRepository
from dto.ResponseDto import ResponseDto


class PriceFluctuationService:
    def __init__(self, app):
        self.app = app
        self.repository = AdvertisementRepository(app)

    def calcultae_mean_price(self, prices):
        price_sum = 0
        area_sum = 0
        for elem in prices:
            if "None" not in str(elem):
                if "(1.0," not in str(elem):
                    data = str(elem).split(', ')
                    elem_price = int(str(data[0])[1:-2])
                    elem_area = int(str(data[1])[:-1])
                    price_sum += elem_price
                    area_sum += elem_area
        if (len(prices) > 0):
            return price_sum / area_sum
        else :
            return -1

    def contruct_mean_price_list(self, price1, price2, price3, price4):
        mean_price_list = []

        mean_price_list.append(self.calcultae_mean_price(price1))
        mean_price_list.append(self.calcultae_mean_price(price2))
        mean_price_list.append(self.calcultae_mean_price(price3))
        mean_price_list.append(self.calcultae_mean_price(price4))
        return mean_price_list

    def define_price_fluctuation(self, nr_rooms, construction_year, distributor):
        today = DT.date.today()
        price_list1 = self.repository.getAdvertisementPricesForDateBetween(today - DT.timedelta(days=28), today - DT.timedelta(days=21))
        price_list2 = self.repository.getAdvertisementPricesForDateBetween(today - DT.timedelta(days=21), today - DT.timedelta(days=14))
        price_list3 = self.repository.getAdvertisementPricesForDateBetween(today - DT.timedelta(days=14), today - DT.timedelta(days=7))
        price_list4 = self.repository.getAdvertisementPricesForDateBetween(today - DT.timedelta(days=7), today)
        mean_price_list = self.contruct_mean_price_list(price_list1, price_list2, price_list3, price_list4)

        preference_price_list1 = self.repository.getAdvertisementPricesForDateBetweenAndPreferences(today - DT.timedelta(days=28), today - DT.timedelta(days=21), nr_rooms, construction_year, distributor)
        preference_price_list2 = self.repository.getAdvertisementPricesForDateBetweenAndPreferences(today - DT.timedelta(days=21), today - DT.timedelta(days=14), nr_rooms, construction_year, distributor)
        preference_price_list3 = self.repository.getAdvertisementPricesForDateBetweenAndPreferences(today - DT.timedelta(days=14), today - DT.timedelta(days=7), nr_rooms, construction_year, distributor)
        preference_price_list4 = self.repository.getAdvertisementPricesForDateBetweenAndPreferences(today - DT.timedelta(days=7), today, nr_rooms, construction_year, distributor)
        preference_mean_price_list = self.contruct_mean_price_list(preference_price_list1, preference_price_list2, preference_price_list3, preference_price_list4)

        if preference_mean_price_list[0] == -1:
            preference_mean_price_list[0] = mean_price_list[0]
        if preference_mean_price_list[1] == -1:
            preference_mean_price_list[1] = mean_price_list[1]
        if preference_mean_price_list[2] == -1:
            preference_mean_price_list[2] = mean_price_list[2]
        if preference_mean_price_list[3] == -1:
            preference_mean_price_list[3] = mean_price_list[3]

        date_list = [str(today - DT.timedelta(days=21)), str(today - DT.timedelta(days=14)), str(today - DT.timedelta(days=7)), str(today)]
        test = ResponseDto(date_list, mean_price_list, preference_mean_price_list)
        return test
