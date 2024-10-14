using AccountNullLog;

var nullLog = new Account(new NullLog());
nullLog.SomeOperation();