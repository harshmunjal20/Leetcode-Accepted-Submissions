class TextEditor {
private:
    string ans;
    int idx;
public:
    TextEditor() {
        ans = "";
        idx = 0;
    }
    
    void addText(string text) {
        ans.insert(idx, text);
        idx += text.size();
    }
    
    int deleteText(int k) {
        int actualCharsDeleted = k;
        if (idx - k < 0) actualCharsDeleted = idx;
        idx = max(0, idx - k);
        ans.erase(idx, actualCharsDeleted);
        return actualCharsDeleted;
    }
    
    string cursorLeft(int k) {
        if (idx - k < 0) idx = 0;
        else idx = idx - k;

        if (idx >= 10) {
            return ans.substr(idx - 10, 10);
        }
        else {
            return ans.substr(0, idx);
        }
    }
    
    string cursorRight(int k) {
        if (idx + k <= ans.size()) {
            idx += k;
        }
        else {
            idx = ans.size();
        }

        if (idx >= 10) {
            return ans.substr(idx - 10, 10);
        }
        else {
            return ans.substr(0, idx);
        }
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */