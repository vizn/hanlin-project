import { Composition } from "remotion";

// 学校信息常量
const SCHOOL_INFO = {
  name: "Philippine Pasay Chung Hua Academy",
  tagline: "Help Your Child Become A Well-Rounded Individual",
  foundationYear: "89th Foundation Day",
  mission: [
    "PROVIDE high-quality education",
    "PROMOTE holistic development",
    "CULTIVATE professional skills",
    "HELP students achieve success"
  ],
  programs: ["Preschool", "Elementary", "Secondary", "Chinese Language Arts", "Computer Program"],
  contact: {
    address: "2269 A.Luna, Pasay, 1300 Metro Manila",
    phone: "+87-88311773"
  }
};

// 主应用程序组件 - 使用 Remotion 原生 API
const App = () => {
  return (
    <Composition
      id="PPCHA_Promotional_Video"
      component={App}
      durationInMinutes={3}
      defaultSize={[1920, 1080]}
      fps={60}
      format="mp4"
      background="#0a1628"
    />
  );
};

export default App;
