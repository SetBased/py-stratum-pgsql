from cleo import CommandTester
from pystratum_cli.application.StratumApplication import StratumApplication

from test.StratumTestCase import StratumTestCase


class AAATest(StratumTestCase):
    """
    This test must run before all other tests because this test loads the stored routines.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test1(self):
        """
        Runs the stratum command: loads the stored routines and generates the stored routine wrapper.
        """
        application = StratumApplication()
        command = application.find('stratum')
        command_tester = CommandTester(command)
        status = command_tester.execute([('command', command.get_name()),
                                         ('config_file', 'test/etc/stratum.cfg')])

        self.assertEqual(0, status)

# ----------------------------------------------------------------------------------------------------------------------
