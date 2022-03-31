from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop('HarryS')

    def test_constructor(self):
        self.assertEqual('HarryS', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_if_given_quantity_that_is_less_or_equal_to_zero(self):
        for param in [0, -1]:
            with self.assertRaises(ValueError) as cm:
                self.shop.add_food('meat', param)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(cm.exception))

    def test_add_food_when_the_given_food_is_not_in(self):
        result = self.shop.add_food('meat', 1)
        self.assertEqual({'meat': 1}, self.shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", result)

    def test_add_food_when_the_given_food_is_in(self):
        self.shop.food = {'meat': 1}
        result = self.shop.add_food('meat', 1)
        self.assertEqual({'meat': 2}, self.shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", result)

    def test_add_pet_if_the_pet_name_is_already_present_raises_error(self):
        self.shop.pets = ['Garry']
        with self.assertRaises(Exception) as cm:
            self.shop.add_pet('Garry')
        self.assertEqual('Cannot add a pet with the same name', str(cm.exception))

    def test_add_pet_if_the_pet_name_is_not_present_in_the_shop(self):
        result = self.shop.add_pet('Garry')
        self.assertEqual(['Garry'], self.shop.pets)
        self.assertEqual("Successfully added Garry.", result)

    def test_feed_pet_if_the_given_pet_name_is_not_present_raises_error(self):
        with self.assertRaises(Exception) as cm:
            self.shop.feed_pet('meat', 'Garry')
        self.assertEqual('Please insert a valid pet name', str(cm.exception))

    def test_feed_pet_if_the_given_food_is_not_present_returns_that_we_do_not_have_that_food(self):
        self.shop.pets = ['Garry']
        result = self.shop.feed_pet('meat', 'Garry')
        self.assertEqual('You do not have meat', result)

    def test_feed_pet_if_the_food_quantity_of_the_given_food_is_less_than_100_adds_more_of_that_food(self):
        self.shop.food = {'meat': 99}
        self.shop.pets = ['Garry']
        result = self.shop.feed_pet('meat', 'Garry')
        self.assertEqual(1099.0, self.shop.food['meat'])
        self.assertEqual('Adding food...', result)

    def test_feed_pet_feeds_pet_and_removes_food(self):
        self.shop.food = {'meat': 100}
        self.shop.pets = ['Garry']
        result = self.shop.feed_pet('meat', 'Garry')
        self.assertEqual({'meat': 0}, self.shop.food)
        self.assertEqual('Garry was successfully fed', result)

    def test_repr(self):
        self.shop.pets = ['Garry', 'Tom']
        result = repr(self.shop)
        self.assertEqual('Shop HarryS:\nPets: Garry, Tom', result)

if __name__ == '__main__':
    main()