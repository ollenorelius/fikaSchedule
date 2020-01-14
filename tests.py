import unittest
import freezegun
import app.DateController
import app.StateModel
import time

class TestDateStuff(unittest.TestCase):
    def test_test(self):
        self.assertEqual("a", "a")

    def test_date_controller(self):
        freezer = freezegun.freeze_time("2019-10-23 23:59:59")
        freezer.start()
        state_model = app.StateModel.StateModel("test_state")
        date_controller = app.DateController.DateController(state_model)

        start_week_in_state = state_model.state["index"]
        date_controller.check_date()
        self.assertEqual(start_week_in_state, state_model.state["index"])
        freezer.stop()
        time.sleep(2)
        date_controller.check_date()
        self.assertNotEqual(start_week_in_state, state_model.state["index"])


        
if __name__ == "__main__":
    unittest.main()
