class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        total = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total, 1)

    def calculate_washing_price(self, car: Car) -> float:
        income = (car.comfort_class * (self.clean_power - car.clean_mark)
                  * self.average_rating / self.distance_from_city_center)
        return round(income, 1)

    def wash_single_car(self, car: Car) -> float:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rate: float) -> None:
        total_rating = self.average_rating * self.count_of_ratings
        new_total_rating = total_rating + rate
        new_middle_rating = new_total_rating / (self.count_of_ratings + 1)
        self.average_rating = round(new_middle_rating, 1)
        self.count_of_ratings += 1
