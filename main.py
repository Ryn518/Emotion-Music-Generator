import mido
from mido import Message, MidiFile, MidiTrack
import random

# 情绪到音符的映射规则 
emotion_scale = {
    "happy": {"notes": [60, 62, 64, 67, 69], "tempo": 140}, # C大调音阶，较快节奏
    "sad": {"notes": [60, 63, 65, 67], "tempo": 70}, # 小调色彩，慢节奏
    "excited": {"notes": [60, 64, 65, 67, 72], "tempo": 180} # 高音，快节奏
}

def generate_music(emotion):
    """
    根据情绪生成一段MIDI音乐
    """
    if emotion not in emotion_scale:
        print("情绪不支持，请尝试 'happy', 'sad', 或 'excited'")
        return

    config = emotion_scale[emotion]
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # 设置节奏
    track.append(Message('program_change', program=0, time=0))

    # 生成一段随机旋律
    for i in range(16): # 生成16个音符
        note = random.choice(config["notes"])
        # 音符开
        track.append(Message('note_on', channel=0, note=note, velocity=64, time=32))
        # 音符关
        track.append(Message('note_off', channel=0, note=note, velocity=127, time=160))

    # 保存MIDI文件
    midi_filename = f"{emotion}_music.mid"
    mid.save(midi_filename)
    print(f"✅ {emotion}情绪的音乐已生成并保存为: {midi_filename}")
    return midi_filename

if __name__ == "__main__":
    user_emotion = input("请输入你的情绪 (happy/sad/excited): ").lower()
    generate_music(user_emotion)