import { FaceWidgets } from "../../components/widgets/FaceWidgets";

export default function FacePage() {
  return (
    <div className="px-6 pt-10 pb-20 sm:px-10 md:px-14">
      <div className="text-center pb-6 text-2xl font-medium text-neutral-800">Speak once you are ready.</div>
      <FaceWidgets />
    </div>
  );
}
