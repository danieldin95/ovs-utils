# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import time
import threading
import sys

from ovs_tools.common.prog import ovs_vsctl


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interface",
                    help="watch on interface.")
parser.add_argument("-n", "--interval", default=2, type=int,
                    help="interval time per second")
args = parser.parse_args()


def monitor():
    pass


def run():
    while True:
        out = ovs_vsctl("get interface {} statistics".format(args.interface))
        sys.stdout.write(out + "\n")
        time.sleep(args.interval)


def setup():
    x = threading.Thread(target=run)
    x.setDaemon(True)
    x.start()

    j = threading.Thread(target=monitor)
    j.setDaemon(True)
    j.start()


def main():
    setup()
    while True:
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        raise
