class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> result(n, 0);
        stack<int> st;
        int prevTime = 0;

        for (string& log : logs) 
        {
            int id, time;
            string type;

            int firstColon = log.find(':');
            int secondColon = log.find(':', firstColon + 1);

            id = stoi(log.substr(0, firstColon));
            type = log.substr(firstColon + 1, secondColon - firstColon - 1);
            time = stoi(log.substr(secondColon + 1));

            if (type == "start") 
            {
                if (!st.empty()) 
                {
                    result[st.top()] += time - prevTime;
                }
                st.push(id);
                prevTime = time;
            } else {
                result[st.top()] += time - prevTime + 1;
                st.pop();
                prevTime = time + 1;
            }
        }

        return result;
    }
};