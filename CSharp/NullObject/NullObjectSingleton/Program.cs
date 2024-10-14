using NullObjectSingleton;

ILog log = new Log();
var nullObjectInstance = log.Null;
nullObjectInstance.Warn();