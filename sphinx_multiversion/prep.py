import logging
import subprocess
import sys

def prep_commands(commands, root_dir, target_dir):
    """ Prepare the target directories after they've been checked out by
    running a set of commands

    Text subsitutions that can be used: _root_, _target_

    Commands are run in target directory
    """

    logger = logging.getLogger(__name__)

    for cmd in commands:
        # replace directory path strings
        rep_cmd = cmd.replace('_root_', root_dir).replace('_target_', target_dir)

        # run the command
        try:
            logger.info("Running prep command: '%s'" % rep_cmd)
            subprocess.check_call(rep_cmd.split(), cwd=target_dir)

        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            logger.error("Prep command '%s' failed: %s", rep_cmd, exc.output)
            sys.exit(1)
