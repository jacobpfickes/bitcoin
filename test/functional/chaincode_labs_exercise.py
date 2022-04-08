#!/usr/bin/env python3
# Copyright (c) 2017-2021 The Bitcoin Core developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.
"""Chaincode Labs Exercise

Mine a block on node 0, send it to node 1, and check that node 1 recieved it.
"""

# Avoid wildcard * imports
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import (
    assert_equal,
)

class ExampleTest(BitcoinTestFramework):
    def set_test_params(self):
        # create 2 nodes with a clean chain (starting at the genesis block)
        self.setup_clean_chain = True
        self.num_nodes = 2

    def setup_network(self):
        # setup nodes but don't connect (we will do this later)
        self.setup_nodes()

    def run_test(self):
        """Main test logic"""

        self.log.info("Starting test!")

        self.log.info("Mine an extra block on node 0")
        # Mine an extra block on node 0
        self.generate(self.nodes[0], sync_fun=self.no_op, nblocks=1)
        # assert node 0 and 1 no longer match because of the newly mined block
        assert self.nodes[0].getbestblockhash() != self.nodes[1].getbestblockhash()

        self.log.info("Sync new block from node 0 to node 1")
        # new block is sent from node 0 to node 1 because of automatic syncing when nodes are connected
        self.connect_nodes(0, 1)

        self.log.info("assert node 0 and node 1 match")  
        # assert new block is on node 2      
        assert_equal(self.nodes[0].getbestblockhash(), self.nodes[1].getbestblockhash())


if __name__ == '__main__':
    ExampleTest().main()
