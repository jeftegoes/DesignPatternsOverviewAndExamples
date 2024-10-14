namespace BeyondElvisOperator
{
    public static class Maybe
    {
        public static TResult With<TInput, TResult>(this TInput o,
                                                    Func<TInput, TResult> evaluator) where TResult : class where TInput : class
        {
            if (o == null) return null;
            else return evaluator(o);
        }

        public static TInput If<TInput>(this TInput o,
                                        Func<TInput, bool> evaluator) where TInput : class
        {
            if (o == null) return null;
            return evaluator(o) ? o : null;
        }

        public static TInput Do<TInput>(this TInput o,
                                        Action<TInput> action) where TInput : class
        {
            if (o == null) return null;

            action(o);

            return o;
        }

        public static TResult Return<TInput, TResult>(this TInput o,
                                                      Func<TInput, TResult> evaluator,
                                                      TResult failureValue) where TInput : class
        {
            if (o == null) return failureValue;
            return evaluator(o);
        }

        public static TResult WithValue<TInput, TResult>(this TInput o,
                                                         Func<TInput, TResult> evaluator) where TInput : struct
        {
            return evaluator(o);
        }
    }
}