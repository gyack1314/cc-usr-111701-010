"""冻结门户标签页与动作上下文。"""
class PortalReplay:
    def __init__(self, steps):
        self.steps=list(steps)
        self.position=0
        self.tabs={}
        self.actions=[]
    def next(self, action, tab, principal, draft):
        if self.position>=len(self.steps):raise EOFError('没有后续门户响应')
        expected=self.steps[self.position]
        if (action,tab,principal,draft)!=(expected['action'],expected['tab'],expected['principal'],expected['draft']):
            raise ValueError('门户动作与冻结记录不符')
        self.position+=1
        result=expected['response']
        self.tabs[tab]={'principal':principal,'draft':draft,'revision':result['revision']}
        self.actions.append({'action':action,'tab':tab,'principal':principal,'draft':draft,'revision':result['revision']})
        return result
