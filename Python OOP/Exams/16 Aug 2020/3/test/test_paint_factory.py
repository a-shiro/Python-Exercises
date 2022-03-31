from project import PaintFactory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('TestFactory', 3)
        self.factory.valid_ingredients = ["blue", "green", "red"]

    def test_constructor(self):
        self.assertEqual('TestFactory', self.factory.name)
        self.assertEqual(3, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["blue", "green", "red"], self.factory.valid_ingredients)

    def test_repr_returns_correct_str_with_no_ingredients(self):
        result = repr(self.factory)
        self.assertEqual(f'Factory name: {self.factory.name} with capacity {self.factory.capacity}.\n', result)

    def test_repr_returns_correct_str_with_ingredients(self):
        self.factory.ingredients = {'Yellow': 2}
        result = repr(self.factory)

        self.assertEqual(f'Factory name: {self.factory.name} '
                         f'with capacity {self.factory.capacity}.\nYellow: 2\n', result)

    def test_products_property_return_ingredients(self):
        # without ingredient
        result = self.factory.products
        self.assertEqual({}, result)

        # with ingredient
        self.factory.ingredients = {'Red': 1}
        result = self.factory.products
        self.assertEqual({'Red': 1}, result)

    def test_can_add_returns_true(self):
        self.assertTrue(self.factory.can_add(3))

    def test_can_add_returns_false(self):
        self.assertFalse(self.factory.can_add(10))

    def test_add_ingredient_with_an_invalid_ingredient_raises_error(self):
        with self.assertRaises(TypeError) as cm:
            self.factory.add_ingredient('purple', 1)
        self.assertEqual('Ingredient of type purple not allowed in PaintFactory', str(cm.exception))

    def test_add_ingredient_tries_to_add_over_the_capacity_raises_error(self):
        with self.assertRaises(ValueError) as cm:
            self.factory.add_ingredient('blue', 4)
        self.assertEqual('Not enough space in factory', str(cm.exception))

    def test_add_ingredient_with_the_correct_ingredient_and_amount(self):
        self.factory.add_ingredient('blue', 3)
        self.assertEqual({'blue': 3}, self.factory.ingredients)

    def test_remove_ingredient_when_given_a_product_that_is_not_in_ingredients_raises_error(self):
        with self.assertRaises(KeyError) as cm:
            self.factory.remove_ingredient('brown', 3)
        self.assertEqual("'No such ingredient in the factory'", str(cm.exception))

    def test_remove_ingredient_when_given_a_product_quantity_more_than_we_have_raises_error(self):
        self.factory.ingredients = {'red': 1}
        with self.assertRaises(ValueError) as cm:
            self.factory.remove_ingredient('red', 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(cm.exception))

    def test_remove_ingredient_subtracts_the_given_quantity_correctly(self):
        self.factory.ingredients = {'red': 3}
        self.factory.remove_ingredient('red', 2)
        self.assertEqual({'red': 1}, self.factory.ingredients)


if __name__ == '__main__':
    main()