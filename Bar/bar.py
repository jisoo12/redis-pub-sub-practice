from revent import Producer
import redis

class Bar():
    # ep = Producer("bar", host="localhost", port=6379, db=0)
    
    # @ep.event("update")
    # def bar_action(self, foo, **kwargs):
    #     print("BAR ACTION")
    #     # ep.send_event("update", {"test": str(True)})
    #     return "BAR ACTION"

    def bar_action(foo, **kwargs):
        ep = Producer("bar", host="localhost", port=6379, db=0)
        print("BAR ACTION")
        kwargs['foo'] = foo
        ep.send_event("update", kwargs)
        return "BAR ACTION"

# if __name__ == '__main__':
#     Bar().bar_action("test", test="True")