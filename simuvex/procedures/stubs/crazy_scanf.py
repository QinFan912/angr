import simuvex

class crazy_scanf(simuvex.SimProcedure):
    #pylint:disable=arguments-differ

    def run(self, src, fmt, one, two, three): #pylint:disable=unused-argument
        memcpy = simuvex.SimProcedures['libc.so.6']['memcpy']

        self.inline_call(memcpy, one, src, 5)
        self.state.store_mem(one+4, self.state.BVV(0, 8))
        self.inline_call(memcpy, two, src+6, 8192)
        self.state.store_mem(two+8191, self.state.BVV(0, 8))
        self.inline_call(memcpy, three, src+6+8193, 12)
        self.state.store_mem(three+11, self.state.BVV(0, 8))

        #if simuvex.o.SYMBOLIC in self.state.options:
        #     #crazy_str = "index.asp?authorization=M3NhZG1pbjoyNzk4ODMwMw==&yan=yes\x00"
        #     #crazy_str = "index.asp?authorization=3sadmin:27988303&yan=yes\x00"
        #     crazy_str = "authorization=3sadmin:27988303\x00"
        #     self.state.add_constraints(self.state.mem_expr(two, len(crazy_str)) == self.state.BVV(crazy_str))

        return self.state.BVV(3)
