namespace LocalInversionOfControl
{
    public struct BoolMarker<T>
    {
        public bool Result;
        public T Self;
        internal Operation PendingOp;

        public static implicit operator bool(BoolMarker<T> maker)
        {
            return maker.Result;
        }

        public BoolMarker<T> And => new BoolMarker<T>(this.Result, Self, Operation.And);

        public BoolMarker(bool result, T self, Operation pendingOp)
        {
            Result = result;
            Self = self;
            PendingOp = pendingOp;
        }

        public BoolMarker(bool result, T self) : this(result, self, Operation.None)
        {
            Result = result;
            Self = self;
        }
    }
}