from revent import Producer
import redis

class Foo():
    # ep = Producer("foo", host="localhost", port=6379, db=0)
    
    # @ep.event("update")
    # def bar_action(self, bar, **kwargs):
    #     print("FOO ACTION")
    #     # ep.send_event("update", {"test": str(True)})
    #     return "FOO ACTION"

    def foo_action(bar, **kwargs):
        ep = Producer("foo", host="localhost", port=6379, db=0)
        print("FOO ACTION")
        kwargs['bar'] = bar
        ep.send_event("update", kwargs)
        return "FOO ACTION"

# if __name__ == '__main__':
#     Foo().bar_action("test", test="True")