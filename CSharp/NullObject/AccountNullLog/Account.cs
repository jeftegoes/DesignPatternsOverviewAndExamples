namespace AccountNullLog
{
    public class Account
    {
        private ILog _log;

        public Account(ILog log)
        {
            _log = log;
        }

        public void SomeOperation()
        {
            var c = _log.RecordCount;
            _log.LogInfo("Performing an operation");
            
            if (c + 1 != _log.RecordCount)
                throw new Exception();

            if (_log.RecordCount >= _log.RecordLimit)
                throw new Exception();
        }
    }
}