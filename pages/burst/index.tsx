import { BurstWidgets } from "../../components/widgets/BurstWidgets";

export default function BurstPage() {
  return (
    <div className="flex flex-col items-center px-6 pt-10 pb-20 sm:px-10 md:px-14">
      <div className="text-center pb-3 text-2xl font-medium text-neutral-800">
        Audio only
      </div>
      <div className="text-center pb-6">Speak once you are ready.</div>
      <BurstWidgets />
    </div>
  );
}
