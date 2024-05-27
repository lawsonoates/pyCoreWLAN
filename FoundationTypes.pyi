from typing import NewType

NSInteger = NewType('NSInteger', int)
NSIntegerMax = NewType('NSIntegerMax', int)
NSUInteger = NewType('NSUInteger', int)
NSString = NewType('NSString', str)
NSData = NewType('NSData', bytes)
NSError = NewType('NSError', Exception)

NSDictionary = NewType('NSDictionary', dict)
NSOrderedSet = NewType('NSOrderedSet', set)

SecIdentityRef = NewType('SecIdentityRef', object)
CFArrayRef = NewType('CFArrayRef', list)
CFStringRef = NewType('CFStringRef', str)
CFDataRef = NewType('CFDataRef', bytes)
OSStatus = int

CWEventType = NewType('CWEventType', int)