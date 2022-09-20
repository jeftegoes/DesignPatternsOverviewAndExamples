namespace LocalInversionOfControl
{
    public static class ExtensionMethods
    {
        public static T AddTo<T>(this T self, params ICollection<T>[] colls)
        {
            foreach (var coll in colls)
                coll.Add(self);

            return self;
        }

        public static bool IsOneOf<T>(this T self, params T[] values)
        {
            return values.Contains(self);
        }

        public static BoolMarker<TSubject> HasNo<TSubject, T>(this TSubject self, Func<TSubject, IEnumerable<T>> props)
        {
            return new BoolMarker<TSubject>(!props(self).Any(), self);
        }

        public static BoolMarker<TSubject> HasSome<TSubject, T>(this TSubject self, Func<TSubject, IEnumerable<T>> props)
        {
            return new BoolMarker<TSubject>(props(self).Any(), self);
        }

        public static BoolMarker<T> HasNo<T, U>(this BoolMarker<T> marker, Func<T, IEnumerable<U>> props)
        {
            if (marker.PendingOp == Operation.And && !marker.Result)
                return marker;
                
            return new BoolMarker<T>(!props(marker.Self).Any(), marker.Self);
        }
    }
}