import os
import sys
import unittest


class OelintLinking(unittest.TestCase):

    RECIPE_1 = os.path.join(os.path.dirname(__file__), "testlayer/recipes-bar/test_1.bb")
    RECIPE_2 = os.path.join(os.path.dirname(__file__), "testlayer/recipes-bar/test_2.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_linking(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintLinking.RECIPE_1)
        self.__stash.AddFile(OelintLinking.RECIPE_2)
        self.__stash.Finalize()

        _stash = self.__stash.GetItemsFor(filename=OelintLinking.RECIPE_1, nolink=True)
        self.assertTrue(_stash, msg="Stash has items")
        for x in _stash:
            _links = sorted(os.path.basename(y) for y in x.Links)
            self.assertEqual(_links, ['global-foo.bbclass', 'recipe-foo.bbclass', 'test.inc', 'test2.inc'])

        _stash = self.__stash.GetItemsFor(filename=OelintLinking.RECIPE_2, nolink=True)
        self.assertTrue(_stash, msg="Stash has items")
        for x in _stash:
            _links = sorted(os.path.basename(y) for y in x.Links)
            self.assertEqual(_links, ['global-foo.bbclass', 'recipe-foo.bbclass', 'test.inc', 'test2.inc', 'test3.inc'])


if __name__ == "__main__":
    unittest.main()
