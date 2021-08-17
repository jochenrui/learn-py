# Singleton Pattern

Create one-of-a-kind objects which have only 1 instance at a time

# Reason

Some objects we only need one, e.g. threadh pool, cache, dialog box, setting handler, ...
-> prevent unexpected behavior that might occur when multiple instances are active

# Bad Fix
1 global instance of the object that's always active -> might cause performance problems

# Better Fix
Object is only created when it's needed